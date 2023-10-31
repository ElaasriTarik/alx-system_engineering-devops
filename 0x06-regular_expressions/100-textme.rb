#!/usr/bin/env ruby
# hbttn

Form1 = ARGV[0].scan(/from:(.\w+)/)
Form2 = ARGV[0].scan(/to:(.\w+)/)
Form3 = ARGV[0].scan(/flags:([0-9:-]+)/)

puts [Form1.compact, Form2.compact, Form3.compact].join(',')
