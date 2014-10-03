# case 1, align

{
  key:       'value',
  test:      'value',
  key:       100,
  test_call: method(1, 2),
}

# case 2, align

{
  'test'      => 'value',
  'test'      => 'value',
  'key'       => 100,
  'test_call' => method(1, 2),
}

# case 3, unalign

{
  key: 'value',
  test: 'value',
  key: 100,
  test_call: method(1, 2),
}

# case 4, unalign

{
  'test' => 'value',
  'test' => 'value',
  'key' => 100,
  'test_call' => method(1, 2),
}