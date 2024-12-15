#!/usr/bin/env ruby
# This script matches a specific pattern using repetition token #0

puts ARGV[0].scan(/hbt{2,5}n/).join
