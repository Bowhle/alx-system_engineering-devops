#!/usr/bin/env ruby
# Match the sender, receiver, and flags in the input text

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
