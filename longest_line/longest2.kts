import java.io.File

var line = ""
var len = 0
File(args[0]).forEachLine {
    if (it.length > len) {
        line = it
        len = it.length
    }
}

println("$line")