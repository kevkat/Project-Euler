  val ts = Array.fill(1e6.toInt)(1)
  
  def count(n: Long, c: Int): Int = 
      if (n==1L || (n < 1e6.toLong && ts(n.toInt) != 1)) c+ts(n.toInt) else 
        count(if (n%2 == 0) n/2 else 3*n+1, c+1)
  
  def processIt(s: Stream[Int], p: (Int, Int)): (Int, Int) = {
    val h = s.head
    if (h >= 1e6) p else {
      val nc = count(h.toLong, 0)
      processIt(s.tail, if (nc>p._2) Pair(h,nc) else p)
    }
  }
  
  val result = processIt(Stream.from(1), Pair(1,1))._1