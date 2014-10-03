import sublime
import sublime_plugin
from Statement import statement
import re

class AlignHashTable(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command('unalign_hash_table')
    for sel in self.view.sel():
      self._align(edit, sel)

  def _align(self, edit, sel):
    arguments = statement.get_arguments(self.view, sel.b)
    tokens = [None] * len(arguments)
    max = None
    for index, argument in enumerate(reversed(arguments)):
      current_tokens = statement.get_tokens(self.view, argument[0], argument)

      if len(current_tokens) <= 1:
        continue

      tokens[index] = current_tokens
      token_length = current_tokens[0][1] - current_tokens[0][0]
      if max == None or max < token_length:
        max = token_length

    if max == None:
      return

    for current_tokens in tokens:
      region = sublime.Region(current_tokens[0][1], current_tokens[1][0])
      delimeter = self.view.substr(region)
      spaces = ' ' * (max - (current_tokens[0][1] - current_tokens[0][0]))
      if delimeter.strip() == ':':
        delimeter += spaces
      else:
        delimeter = spaces + delimeter
      self.view.replace(edit, region, delimeter)

class UnalignHashTable(sublime_plugin.TextCommand):
  def run(self, edit):
    for sel in self.view.sel():
      self._unalign(edit, sel)

  def _unalign(self, edit, sel):
    arguments = statement.get_arguments(self.view, sel.b)
    tokens = [None] * len(arguments)
    max = None
    for index, argument in enumerate(reversed(arguments)):
      current_tokens = statement.get_tokens(self.view, argument[0], argument)

      if len(current_tokens) <= 1:
        continue

      tokens[index] = current_tokens
      token_length = current_tokens[0][1] - current_tokens[0][0]
      if max == None or max < token_length:
        max = token_length

    if max == None:
      return

    for current_tokens in tokens:
      region = sublime.Region(current_tokens[0][1], current_tokens[1][0])
      delimeter = self.view.substr(region)
      spaces = ' ' * (max - (current_tokens[0][1] - current_tokens[0][0]))
      delimeter = re.sub(r'^\s+', ' ', delimeter)
      delimeter = re.sub(r'\s+$', ' ', delimeter)
      self.view.replace(edit, region, delimeter)