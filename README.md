# hayatmoji

An emoji guide for **my** commit messages. 🫣

## About

[Hayatmoji](https://moji.hayatro.id/) is an initiative to standardize and explain **the use of :person_facepalming: on GitHub commit messages**.

The hayatmojis are published on the [following package](https://crates.io/crates/hayatmoji-cli) in order to be used as a dependency 📦.

## Using [hayatmoji-cli](https://github.com/hayatroid/hayatmoji-cli)

To use hayatmojis from your command line install [hayatmoji-cli](https://github.com/hayatroid/hayatmoji-cli). A hayatmoji interactive client for using emojis on commit messages.

```bash
cargo install hayatmoji-cli
```

## Example of usage

In case you need some ideas to integrate hayatmoji in your project, here's a practical way to use it:

```
<intention> [scope?][:?] <message>
```

- `intention`: An emoji from the list.
- `scope`: An optional string that adds contextual information for the scope of the change.
- `message`: A brief explanation of the change.
