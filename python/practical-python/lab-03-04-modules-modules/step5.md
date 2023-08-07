# Module Execution

When a module is imported, _all of the statements in the module execute_ one after another until the end of the file is reached. The contents of the module namespace are all of the _global_ names that are still defined at the end of the execution process. If there are scripting statements that carry out tasks in the global scope (printing, creating files, etc.) you will see them run on import.
