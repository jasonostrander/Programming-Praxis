/*val prices = listOf(100, 80, 70, 65, 95, 120, 150, 75, 95, 100, 110, 120, 90, 80, 85, 90)*/
/*val prices = listOf(100, 80, 70, 65, 95, 120, 150, 75, 95, 100, 110, 120, 90, 80, 85, 90, 34)*/
val prices = listOf(100, 80, 70, 65, 95, 75)

// Functional
val result = prices.mapIndexed {i, a -> prices.subList(i+1, prices.size).map {b ->  Pair(a, b)}}
  .flatten()
  .maxBy {it.second - it.first}
println(result)

// Single scan
var minValue = prices[0]
var maxValue = prices[0]
var maxPrice = 0
for (i in 1..prices.size - 1) {
  if (prices[i] - minValue > maxPrice) {
    maxValue = prices[i]
    maxPrice = maxValue - minValue
  }
  if (i != prices.size - 1 && prices[i] < minValue) minValue = prices[i]
}
println("$minValue $maxValue")
