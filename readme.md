# Sublime AlignHashTable plugin

Aligns hash tables definitions (hashes in ruby, dicts in python, named arrays in
php).


### Demo

![Demo](https://github.com/shagabutdinov/sublime-enhanced-demos/raw/master/align_hash_table.gif "Demo")

### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Aligns hash table definition so all values are positioned under one level.

  ```
  # before
  table = {
    key: value1,
    table_key: value1,
  }

  # after
  table = {
    key:       value1,
    table_key: value1,
  }
  ```


### Usage

Position cursor to hash table that should be aligned. Hit keyboard shortcut or
run commands through command palette to align or to unalign hash table. Note
that if you have nested hash tables only table under cursor on bottom of nesting
(smaller table) will be aligned.


### Commands

| Description        | Keyboard shortcuts | Command palette         |
|--------------------|--------------------|-------------------------|
| Align hash table   | ctrl+m, ctrl+a     | AlignHashTable: align   |
| Unalign hash table | ctrm+m, a          | AlignHashTable: unalign |


### Dependencies

* [statement](https://github.com/shagabutdinov/sublime-statement)