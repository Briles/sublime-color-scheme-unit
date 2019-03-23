from .color_scheme import load_color_scheme_resource


_default_syntaxes = [
    'Packages/Scala/Scala.sublime-syntax',
    'Packages/ShellScript/Shell-Unix-Generic.sublime-syntax',
    'Packages/Rails/SQL (Rails).sublime-syntax',
    'Packages/SQL/SQL.sublime-syntax',
    'Packages/TCL/Tcl.sublime-syntax',
    'Packages/LaTeX/TeX.sublime-syntax',
    'Packages/Textile/Textile.sublime-syntax',
    'Packages/XML/XML.sublime-syntax',
    'Packages/YAML/YAML.sublime-syntax',
    'Packages/ActionScript/ActionScript.sublime-syntax',
    'Packages/AppleScript/AppleScript.sublime-syntax',
    'Packages/ASP/ASP.sublime-syntax',
    'Packages/ShellScript/Bash.sublime-syntax',
    'Packages/Batch File/Batch File.sublime-syntax',
    'Packages/LaTeX/Bibtex.sublime-syntax',
    'Packages/C#/Build.sublime-syntax',
    'Packages/C#/C#.sublime-syntax',
    'Packages/C++/C.sublime-syntax',
    'Packages/C++/C++.sublime-syntax',
    'Packages/OCaml/camlp4.sublime-syntax',
    'Packages/Rust/Cargo.sublime-syntax',
    'Packages/Clojure/Clojure.sublime-syntax',
    'Packages/ShellScript/commands-builtin-shell-bash.sublime-syntax',
    'Packages/CSS/CSS.sublime-syntax',
    'Packages/D/D.sublime-syntax',
    'Packages/Diff/Diff.sublime-syntax',
    'Packages/D/DMD Output.sublime-syntax',
    'Packages/Graphviz/DOT.sublime-syntax',
    'Packages/Erlang/Erlang.sublime-syntax',
    'Packages/Git Formats/Git Attributes.sublime-syntax',
    'Packages/Git Formats/Git Commit.sublime-syntax',
    'Packages/Git Formats/Git Common.sublime-syntax',
    'Packages/Git Formats/Git Config.sublime-syntax',
    'Packages/Git Formats/Git Ignore.sublime-syntax',
    'Packages/Git Formats/Git Link.sublime-syntax',
    'Packages/Git Formats/Git Log.sublime-syntax',
    'Packages/Git Formats/Git Rebase.sublime-syntax',
    'Packages/Go/Go.sublime-syntax',
    'Packages/Groovy/Groovy.sublime-syntax',
    'Packages/Haskell/Haskell.sublime-syntax',
    'Packages/Erlang/HTML (Erlang).sublime-syntax',
    'Packages/Rails/HTML (Rails).sublime-syntax',
    'Packages/TCL/HTML (Tcl).sublime-syntax',
    'Packages/HTML/HTML.sublime-syntax',
    'Packages/ASP/HTML-ASP.sublime-syntax',
    'Packages/Java/Java Server Pages (JSP).sublime-syntax',
    'Packages/Java/Java.sublime-syntax',
    'Packages/Java/JavaDoc.sublime-syntax',
    'Packages/Java/JavaProperties.sublime-syntax',
    'Packages/Rails/JavaScript (Rails).sublime-syntax',
    'Packages/JavaScript/JavaScript.sublime-syntax',
    'Packages/JavaScript/JSON.sublime-syntax',
    'Packages/LaTeX/LaTeX Log.sublime-syntax',
    'Packages/LaTeX/LaTeX.sublime-syntax',
    'Packages/Lisp/Lisp.sublime-syntax',
    'Packages/Haskell/Literate Haskell.sublime-syntax',
    'Packages/Lua/Lua.sublime-syntax',
    'Packages/Makefile/Make Output.sublime-syntax',
    'Packages/Makefile/Makefile.sublime-syntax',
    'Packages/Markdown/Markdown.sublime-syntax',
    'Packages/Matlab/Matlab.sublime-syntax',
    'Packages/Markdown/MultiMarkdown.sublime-syntax',
    'Packages/Objective-C/Objective-C.sublime-syntax',
    'Packages/Objective-C/Objective-C++.sublime-syntax',
    'Packages/OCaml/OCaml.sublime-syntax',
    'Packages/OCaml/OCamllex.sublime-syntax',
    'Packages/OCaml/OCamlyacc.sublime-syntax',
    'Packages/Pascal/Pascal.sublime-syntax',
    'Packages/Perl/Perl.sublime-syntax',
    'Packages/PHP/PHP Source.sublime-syntax',
    'Packages/PHP/PHP.sublime-syntax',
    'Packages/Python/Python.sublime-syntax',
    'Packages/R/R Console.sublime-syntax',
    'Packages/R/R.sublime-syntax',
    'Packages/R/Rd (R Documentation).sublime-syntax',
    'Packages/Regular Expressions/RegExp.sublime-syntax',
    'Packages/JavaScript/Regular Expressions (JavaScript).sublime-syntax',
    'Packages/PHP/Regular Expressions (PHP).sublime-syntax',
    'Packages/Python/Regular Expressions (Python).sublime-syntax',
    'Packages/RestructuredText/reStructuredText.sublime-syntax',
    'Packages/Rails/Ruby Haml.sublime-syntax',
    'Packages/Rails/Ruby on Rails.sublime-syntax',
    'Packages/Ruby/Ruby.sublime-syntax',
    'Packages/Rust/Rust.sublime-syntax',
]

_minimal_syntaxes = [
    'Packages/Ruby/Ruby.sublime-syntax',
    'Packages/C++/C.sublime-syntax',
    'Packages/HTML/HTML.sublime-syntax',
    'Packages/PHP/PHP.sublime-syntax',
    'Packages/Markdown/Markdown.sublime-syntax',
    'Packages/JavaScript/JSON.sublime-syntax',
    'Packages/JavaScript/JavaScript.sublime-syntax',
    'Packages/CSS/CSS.sublime-syntax',
    'Packages/XML/XML.sublime-syntax',
    'Packages/Python/Python.sublime-syntax',
]

_minimal_scopes = [
    'entity.name',
    'entity.other.inherited-class',
    'entity.name.section',
    'entity.name.tag',
    'entity.other.attribute-name',
    'variable',
    'variable.language',
    'variable.parameter',
    'variable.function',
    'constant',
    'constant.numeric',
    'constant.language',
    'constant.character.escape',
    'storage.type',
    'storage.modifier',
    'support',
    'keyword',
    'keyword.control',
    'keyword.operator',
    'keyword.declaration',
    'string',
    'comment',
    'invalid',
    'invalid.deprecated',
]


class Coverage():

    def __init__(self, output, enabled, is_single_file):
        self.output = output
        self.enabled = enabled
        self.is_single_file = is_single_file
        self.tests_info = {}

    def on_test_start(self, test, data):
        settings = data.settings()
        color_scheme = settings.get('color_scheme')
        syntax = settings.get('syntax')
        self.tests_info[test] = {
            'color_scheme': color_scheme,
            'syntax': syntax
        }

    def on_tests_end(self):
        if not self.enabled:
            return

        cs_tested_syntaxes = {}
        for test, info in self.tests_info.items():
            cs = info['color_scheme']
            s = info['syntax']
            if cs not in cs_tested_syntaxes:
                cs_tested_syntaxes[cs] = []
            cs_tested_syntaxes[cs].append(s)

        if not cs_tested_syntaxes:
            return

        self.output.write('\n')
        self.output.write('Generating code coverage report...\n\n')

        report_data = []
        for color_scheme, syntaxes in cs_tested_syntaxes.items():
            color_scheme_json = load_color_scheme_resource(color_scheme)
            syntaxes = set(syntaxes)
            colors = set()
            scopes = set()
            styles = set()
            color_scheme_variables = color_scheme_json['variables']

            for struct in color_scheme_json['rules']:
                if 'scope' in struct:
                    for scope in struct['scope'].split(','):
                        scopes.add(scope.strip())

                if 'foreground' in struct:
                    fg = struct['foreground']
                    color = fg
                    if fg[4:-1] in color_scheme_variables:
                        color = color_scheme_variables[fg[4:-1]]

                    colors.add(color.lower())

                if 'background' in struct:
                    bg = struct['background']
                    color = bg
                    if bg[4:-1] in color_scheme_variables:
                        color = color_scheme_variables[bg[4:-1]]

                    colors.add(color.lower())

                if 'font_style' in struct:
                    if struct['font_style']:
                        styles.add(struct['font_style'])

            report_data.append({
                'color_scheme': color_scheme,
                'syntaxes': syntaxes,
                'default_syntaxes': set(_default_syntaxes) & syntaxes,
                'minimal_syntaxes': set(_minimal_syntaxes) & syntaxes,
                'colors': colors,
                'scopes': scopes,
                'minimal_scopes': set(_minimal_scopes) & scopes,
                'styles': styles
            })

        cs_col_w = max([len(x['color_scheme']) for x in report_data])
        template = '{: <' + str(cs_col_w) + '} {: >20} {: >20}\n'

        self.output.write(template.format('Name', 'Minimal Syntax Tests', 'Minimal Scopes'))
        self.output.write(('-' * cs_col_w) + '------------------------------------------\n')
        for info in sorted(report_data, key=lambda x: x['color_scheme']):
            self.output.write(template.format(
                info['color_scheme'],
                '{} / {}'.format(len(info['minimal_syntaxes']), len(_minimal_syntaxes)),
                '{} / {}'.format(len(info['minimal_scopes']), len(_minimal_scopes))
            ))

        self.output.write('\n')

        for i, info in enumerate(sorted(report_data, key=lambda x: x['color_scheme']), start=1):
            self.output.write('{}) {}\n'.format(i, info['color_scheme']))

            syntaxes_not_covered = [s for s in sorted(_minimal_syntaxes) if s not in info['syntaxes']]
            scopes_not_covered = [s for s in sorted(_minimal_scopes) if s not in info['scopes']]
            total_notice_count = len(scopes_not_covered)
            if not self.is_single_file:
                total_notice_count += len(syntaxes_not_covered)

            if total_notice_count:
                self.output.write('\n')
                self.output.write('   There %s %s notice%s:\n' % (
                    'is' if total_notice_count == 1 else 'are',
                    total_notice_count,
                    '' if total_notice_count == 1 else 's',
                ))

                if syntaxes_not_covered and not self.is_single_file:
                    self.output.write('\n')
                    self.output.write('   Minimal syntaxes tests not covered ({}):\n\n'
                                      .format(len(syntaxes_not_covered)))
                    for i, syntax in enumerate(syntaxes_not_covered, start=1):
                        self.output.write('   * {}\n'.format(syntax))

                if scopes_not_covered:
                    self.output.write('\n')
                    self.output.write('   Minimal scopes not covered ({}):\n\n'.format(len(scopes_not_covered)))
                    for i, scope in enumerate(scopes_not_covered, start=1):
                        self.output.write('   * {}\n'.format(scope))

            self.output.write('\n')

            self.output.write('   Colors   {: >3} {}\n'.format(len(info['colors']), sorted(info['colors'])))

            excluding_alpha = sorted(set([color[0:7] for color in info['colors']]))
            self.output.write('            {: >3} {}\n'.format(len(excluding_alpha), sorted(excluding_alpha)))

            including_alpha = sorted(set([color for color in info['colors'] if len(color) > 7]))
            self.output.write('            {: >3} {}\n'.format(len(including_alpha), sorted(including_alpha)))

            self.output.write('   Styles   {: >3} {}\n'.format(len(info['styles']), sorted(info['styles'])))
            self.output.write('   Syntaxes {: >3} {}\n'.format(len(info['syntaxes']), sorted(info['syntaxes'])))
            self.output.write('   Scopes   {: >3} {}\n'.format(len(info['scopes']), sorted(info['scopes'])))
            self.output.write('\n')

        self.output.write('\n')
