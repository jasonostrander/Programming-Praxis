// Programming praxis: reverse words

def reverse(s:String):String = """([^\s]+)|(\s+)""".r.findAllIn(s).toList.reverse.mkString

assert(reverse("") == "")
assert(reverse(" ") == " ")
assert(reverse("  ") == "  ")
assert(reverse("hello") == "hello")
assert(reverse("hello ") == " hello")
assert(reverse(" hello") == "hello ")
assert(reverse("the quick brown fox") == "fox brown quick the")
assert(reverse("the quick  brown fox") == "fox brown  quick the")
assert(reverse("the quick  brown 42 fox!") == "fox! 42 brown  quick the")
