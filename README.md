# Air File Icons

A clean, minimal file icon theme for Visual Studio Code and Cursor, inspired by the JetBrains New UI (Air) icon set.

![Air File Icons preview](preview-icons.png)

> **Pairs with [Air](https://github.com/franzgollhammer/air-theme-vscode)** — companion color theme (dark + light) ported from JetBrains Air. Designed to look right next to these icons.


## Features

- 112 file type icons, dark + light variants
- Wide language, framework, and config file coverage
- Crisp monochrome-accent style, tuned for compact tree UIs

## Install

### VS Code

1. Extensions panel (`Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Search `Air File Icons`
3. Install
4. `Cmd+Shift+P` / `Ctrl+Shift+P` → `Preferences: File Icon Theme` → `Air File Icons`

### Cursor

Cursor pulls extensions from Open VSX. Same flow: open the Extensions panel, search `Air File Icons`, install, then pick it under `File Icon Theme`.

### Manual (`.vsix`)

Download the latest `.vsix` from [Releases](https://github.com/franzgollhammer/air-icons-vscode/releases), then:

```sh
code --install-extension air-file-icons-<version>.vsix
# or
cursor --install-extension air-file-icons-<version>.vsix
```

## Supported file types

Languages: JavaScript, TypeScript, React, Vue, Svelte, Python, Rust, Go, Java, Kotlin, Swift, C/C++, C#, Ruby, PHP, Dart, Elixir, Haskell, Scala, Clojure, Erlang, Lua, R, Julia, Zig, Nim, OCaml, F#, Groovy, Perl, and more.

Configs: Docker, Git, Webpack, Vite, Rollup, ESLint, Prettier, Babel, TSConfig, npm, pnpm, yarn, bun, Cargo, Maven, Gradle, Bazel, Terraform, Bicep, CMake, and more.

## Development

```sh
npm run dev           # launch VS Code with the extension loaded
npm run dev:insiders  # VS Code Insiders
npm run package       # build .vsix
npm run install:local # package + install into VS Code
```

See [`scripts/`](scripts) for release automation.

## Attribution

Icons derived from [JetBrains intellij-community](https://github.com/JetBrains/intellij-community) (`platform/icons/src/expui/fileTypes/`), licensed under Apache 2.0. See [NOTICE](NOTICE).

## License

[Apache 2.0](LICENSE)
