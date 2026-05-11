package com.verimsolution.hugeiconskmp

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform