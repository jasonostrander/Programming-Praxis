    fun simple(arr: Array<Int>) {
        // first find the max and min values
        var min = Int.MAX_VALUE
        var max = Int.MIN_VALUE
        for (i in arr) {
            if (min > i) {
                min = i
            }
            if (max < i) {
                max = i
            }
        }
        println("Min $min Max $max")

        // then search array for the min
        var t = min + 1
        var i = arr.size - 1
        while (i >= 0) {
            if (arr[i] == t) {
                t += 1
                i = arr.size
            }
            i--
        }
        println("smallest not in array $t")
    }

        fun better(arr: Array<Int>) {
            var min = Int.MAX_VALUE
            var max = Int.MIN_VALUE
            var t = Int.MIN_VALUE
            val hash = mutableMapOf<Int, Boolean>()
            for (i in arr) {
                hash[i] = true
                if (min > i) {
                    min = i
                }
                if (max < i) {
                    max = i
                }
            }
            println("Min $min Max $max")

            for (i in min..max) {
                if (i !in hash) {
                    t = i
                    break
                }
            }
            println("smalled not in array $t")
        }

    simple(arrayOf<Int>(-1, 4, 5, -23, 24))
    simple(arrayOf<Int>(-1, -21, -22, 4, 5, -23, 24))

    better(arrayOf<Int>(-1, 4, 5, -23, 24))
    better(arrayOf<Int>(-1, -21, -22, 4, 5, -23, 24))
