import json

from sublime import load_resource
from sublime import score_selector


def load_color_scheme_resource(color_scheme):
    return json.loads(load_resource(color_scheme))


class ViewStyle():

    def __init__(self, view):
        self.view = view

        self.scope_style_cache = {}

        color_scheme = self.view.settings().get('color_scheme')

        self.json = load_color_scheme_resource(color_scheme)
        variables = self.json['variables']
        self.json_variables_dict = {}

        for var in variables:
            self.json_variables_dict['var({})'.format(var)] = variables[var]

        self.default_styles = {}
        for rule in self.json['rules']:
            if 'scope' not in rule:
                self.default_styles.update(rule['rules'])

    def at_point(self, point):
        scope = self.view.scope_name(point).strip()

        if scope in self.scope_style_cache:
            return self.scope_style_cache[scope]

        style = self.default_styles.copy()

        scored_styles = []
        for rule in self.json['rules']:
            if 'scope' in rule:
                score = score_selector(scope, rule['scope'])

                if 'foreground' in rule:
                    fg = rule['foreground']
                    color = fg
                    if fg in self.json_variables_dict:
                        color = self.json_variables_dict[fg]

                    rule.update({'foreground': color.lower()})

                if 'background' in rule:
                    bg = rule['background']
                    color = bg
                    if bg in self.json_variables_dict:
                        color = self.json_variables_dict[bg]

                    rule.update({'background': color.lower()})

                if 'font_style' in rule:
                    rule.update({'fontStyle': rule['font_style']})

                if score:
                    rule.update({'score': score})
                    scored_styles.append(rule)


        for s in sorted(scored_styles, key=lambda k: k['score']):
            style.update(s)

        self.scope_style_cache[scope] = style

        return style
