import os
import json


skills = [
    "never",
    "array",
    "bool",
    "char",
    "f32",
    "f64",
    "fn",
    "i8",
    "i16",
    "i32",
    "i64",
    "i128",
    "isize",
    "pointer",
    "reference",
    "slice",
    "tuple",
    "u8",
    "u16",
    "u32",
    "u64",
    "u128",
    "unit",
    "usize",
    "assert_matches",
    "async_iter",
    "intrinsics",
    "simd",
    "alloc",
    "any",
    "arch",
    "ascii",
    "backtrace",
    "borrow",
    "boxed",
    "cell",
    "clone",
    "cmp",
    "collections",
    "convert",
    "default",
    "env",
    "error",
    "ffi",
    "fmt",
    "fs",
    "future",
    "hash",
    "hint",
    "io",
    "iter",
    "marker",
    "mem",
    "net",
    "num",
    "ops",
    "option",
    "os",
    "panic",
    "path",
    "pin",
    "prelude",
    "primitive",
    "process",
    "ptr",
    "rc",
    "result",
    "string",
    "sync",
    "task",
    "thread",
    "time",
    "vec",
    "concat_bytes",
    "concat_idents",
    "const_format_args",
    "format_args_nl",
    "log_syntax",
    "trace_macros",
    "assert",
    "assert_eq",
    "assert_ne",
    "cfg",
    "column",
    "compile_error",
    "concat",
    "dbg",
    "debug_assert",
    "debug_assert_eq",
    "debug_assert_ne",
    "eprint",
    "eprintln",
    "format",
    "format_args",
    "include",
    "include_bytes",
    "include_str",
    "x86_64",
    "line",
    "matches",
    "module_path",
    "option_env",
    "print",
    "println",
    "stringify",
    "thread_local",
    "todo",
    "trydeprecated",
    "unimplemented",
    "unreachable",
    "write",
    "writeln",
    "selfty",
    "async",
    "await",
    "break",
    "const",
    "continue",
    "crate",
    "dyn",
    "else",
    "enum",
    "extern",
    "false",
    "for",
    "if",
    "impl",
    "let",
    "loop",
    "match",
    "mod",
    "move",
    "mut",
    "pub",
    "ref",
    "return",
    "self",
    "static",
    "struct",
    "super",
    "trait",
    "true",
    "type",
    "union",
    "unsafe",
    "use",
    "where",
    "while",
    "rustc",
    "rustup",
]


for root, dirs, files in os.walk("./rust"):
    for file in files:
        if file.startswith("step") and file.endswith(".md"):
            file_path = os.path.join(root, file)
            # read the file
            with open(file_path, "r") as f:
                content = f.read()
            file_skills = []
            try:
                # code block begin with ```rust and end with ```
                # each content has multiple code blocks
                if "```rust" in content:
                    code_blocks = content.split("```rust")[1:]
                    for code_block in code_blocks:
                        if "```" in code_block:
                            code_block = code_block.split("```")[0]
                            # remove line breaks
                            code_block = code_block.replace("\n", "")
                            # split by space
                            code_block = code_block.split(" ")
                            for block in code_block:
                                for skill in skills:
                                    if skill in code_block:
                                        file_skills.append(f"rust/{skill}")
            except IndexError:
                pass
            try:
                index_path = os.path.join(root, "index.json")
                with open(index_path, "r") as f:
                    index = json.load(f)
                    steps = index["details"]["steps"]
                    step_index = int(file.split(".")[0].split("step")[1])
                    steps[step_index - 1]["skills"] = list(set(file_skills))
                with open(index_path, "w") as f:
                    json.dump(index, f, indent=2)
            except Exception as e:
                print(file_path)
