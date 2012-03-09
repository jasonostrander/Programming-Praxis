

class RationalNumber(numerator: Int, denominator: Int) {
	require(denominator != 0)
	val n:Int = numerator
	val d:Int = denominator

	override def toString():String = {
		return this.n + "/" + this.d
	}

	def +(a: RationalNumber): RationalNumber = {
		return new RationalNumber(n*a.d + a.n*d, d*a.d)
	}

	def -(a: RationalNumber): RationalNumber = {
		return new RationalNumber(n*a.d - a.n*d, d*a.d)
	}

	def *(a: RationalNumber): RationalNumber = {
		return new RationalNumber(n * a.n, d * a.d)
	}

	def /(a: RationalNumber): RationalNumber = {
		return new RationalNumber(n*a.d / a.n*d, d * a.d)
	}

	def <(a: RationalNumber): Boolean = {
		return n*a.d < a.n * d
	}
}

object Rational extends Application {
	override def main(args:Array[String]) {
		val half = new RationalNumber(1, 2)
		val third = new RationalNumber(2, 3)
		println(half + third)
		println(half < third)
		println(half * third)
		println(half - third)
	}
}
