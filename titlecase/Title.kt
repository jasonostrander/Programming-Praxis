
fun title(s: String): String {
    return s.toLowerCase().split(" ").map { it.substring(0, 1).toUpperCase() + it.substring(1) }.joinToString(" ")
}

fun main(args: Array<String>) {
    val s = "programming PRAXIS"
    assert("Programming Praxis".equals(title(s)))
}
