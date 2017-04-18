import java.io.File

println("${File(args[0]).readLines().maxBy { it.length }}")
