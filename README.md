# config
Small script to manage config files scattered everywhere. God damn RC files.

## Usage
Create `config_map.py` in the same directory as `config.py` if not yet exist.
Add module and config path to `config_map.py`. Example:

```python
config_map = {
    'i3': '~/.config/i3/config',
    'bash': '~/.bashrc',
}
```

Put these two (`config.py` and `config_map.py`) in `$PATH` or symlink `config.py` to somewhere in `$PATH` and there you have it.

## **`$VISUAL`**
`config` uses **`$VISUAL`** if set or fallback to `nvim` (author's favorite editor) if it's unset or empty. You should define one in your shell init file (e.g. `bashrc`) to be consistent with other applications (e.g. `git commit`).
