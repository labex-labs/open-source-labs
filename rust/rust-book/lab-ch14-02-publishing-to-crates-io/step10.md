# Publishing a New Version of an Existing Crate

When you've made changes to your crate and are ready to release a new version, you change the `version` value specified in your `Cargo.toml` file and republish. Use the Semantic Versioning rules at *http://semver.org* to decide what an appropriate next version number is, based on the kinds of changes you've made. Then run `cargo publish` to upload the new version.
