# Modifying capabilities

Libcap and libcap-ng can both be used to modify capabilities.

1. Use libcap to modify the capabilities on a file.

   The command below shows how to set the CAP*NET_RAW capability as \_effective* and _permitted_ on the file represented by `$file`. The `setcap` command calls on libcap to do this.

   ```
   setcap cap_net_raw=ep $file
   ```

2. Use libcap-ng to set the capabilities of a file.

   The `filecap` command calls on libcap-ng.

   ```
   filecap /absolute/path net_raw
   ```

   **Note:** `filecap` requires absolute path names. Shortcuts like `./` are not permitted.
