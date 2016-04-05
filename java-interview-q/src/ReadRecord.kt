import java.io.File

/**
 * Created by j.ostrander on 4/5/16.
 */

data class Record(val id: Int, val score: Int)

fun main(args: Array<String>) {
    val map = mutableMapOf<String, Record>()
    val file = File("record.txt")
    file.forEachLine {
        val (idString, subject, scoreString) = it.split("|")
        val id = Integer.parseInt(idString)
        val score = Integer.parseInt(scoreString)
        val record = map[subject]
        if (record == null) {
            map.put(subject, Record(id, score))
        } else {
            if (record.id > id) {
                map.put(subject, Record(id, score))
            }
        }
    }

    map.forEach { println("${it.key}: ${it.value}")}
}
