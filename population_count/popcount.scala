
var i = args(0).toInt
print(i + " ")
var pop = 0;
while (i > 0) {
      pop += i & 01
      i = i >> 1
}

println(pop)