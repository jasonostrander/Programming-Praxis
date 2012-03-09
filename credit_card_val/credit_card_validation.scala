// Praxis: Credit card validation

def ss(n:Int):Int = {
	n.toString.view.map(_.asDigit).sum
}

def luhn(n:BigInt):Int = {
	val cc = n.toString.view.reverse.zipWithIndex.map( t => (t._2 + 1) match {
		case i if i%2 == 0 => ss(t._1.asDigit*2)
		case _ => t._1.asDigit
	});
	cc.sum
}

def validate(n:BigInt):Boolean = {
	luhn(n) % 10 == 0
}
assert(validate(49927398716L))
assert(!validate(49927398715L))

def addCheck(n:BigInt):BigInt = {
	val t = n.toString.view.mkString
	luhn(BigInt(t+"0"))%10 match {
		case 0 => BigInt(t + "0")
		case x => BigInt(t + (10-x))
	}
}
assert(addCheck(4992739871L) == 49927398716L)
