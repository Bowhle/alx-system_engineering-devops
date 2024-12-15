#!/usr/bin/env ruby
# This script accepts a single argument
# and matches the word "School"

puts ARGV[0].scan(/School/).join
