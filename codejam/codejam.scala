
object CodeJam extends Application {
    def rotate(n:Int, l:List[Int]):List[Int] = l.drop(n) ::: l.take(n)

    def one() = {
        val l = List(5,25,75)
        //(0 until l.length).foreach(l.zip(rotate(_, l)))
    }

    def two(s: String):String = {
        s.split(' ').reverse.mkString(" ")
    }
    
    def t9(c:Char):Int = c match {
        case Seq('a', 'b', 'c') => "abc".indexOf(c)
        case Seq('d', 'e', 'f') => "def".indexOf(c)
        case Seq('g', 'h', 'i') => "ghi".indexOf(c)
        case Seq('j', 'k', 'l') => "jkl".indexOf(c)
        case Seq('m', 'n', 'o') => "mno".indexOf(c)
        case Seq('p', 'q', 'r', 's') => "pqrs".indexOf(c)
        case Seq('t', 'u', 'v') => "tuv".indexOf(c)
        case Seq('w', 'x', 'y', 'z') => "wxyz".indexOf(c)
    }

    def three(s:String):String = {
        s.toLowerCase.foreach(t9)
    }

    override def main(args:Array[String]) {
        println(two("this is a test"))

        println(t9('f'))
    }
}