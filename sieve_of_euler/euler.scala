def eras(l:List[Int]):List[Int] = {
	if (l.isEmpty) return Nil
	l.head :: eras(l.tail.filter(_ % l.head != 0))
}

def euler(l:List[Int]):List[Int] = {
	if (l.isEmpty) return Nil
	val d = l.map(_*l(0))
	val r = l filterNot (d contains)
	l(0) :: euler(r.drop(1))
}

val n = 1000
val l = List.range(2, n)

var t0:Long = System.currentTimeMillis()
eras(l)
var t:Long = System.currentTimeMillis()
println("Eras time = " + (t - t0))

t0 = System.currentTimeMillis()
euler(l)
t = System.currentTimeMillis()
println("Euler time = " + (t-t0))
