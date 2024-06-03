package main

import (
	"fmt"
	"time"
)

var rows = 16
var cols = 32

func mod (a int, b int) int {
    return (a % b + b) % b
}

func CountNeighbors (x int, y int, c [512]int) int {
    count := 0
    for i := -1; i <= 1; i++ {
        for j := -1; j <= 1; j++ {
            if !(i == 0 && j == 0) { // not center of cell
                dx := mod(x + i, cols)
                dy := mod(y + j, rows)
                if (c[(dy * cols) + dx] == 1) {
                    count += 1
                }
            }
        }
    }
    return count
}

func Update (c [512]int) [512]int {
    var ret [512]int
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            nbors := CountNeighbors(x, y, c)
            if c[y*cols + x] == 1 {
                if nbors == 2 || nbors == 3 {
                    ret[y*cols + x] = 1
                } else {
                    ret[y*cols + x] = 0
                }
            } else {
                if nbors == 3 {
                    ret[y*cols + x] = 1
                } else {
                    ret[y*cols + x] = 0
                }
            }
        }
    }
    return ret
}

func Display(c [512]int) {
    for y := 0; y < rows; y++ {
        for x := 0; x < cols; x++ {
            str := "."
            if c[(y * cols) + x] == 1 {
                str = "x"
            }
            fmt.Print(str)
        }
        fmt.Print("\n")
    }
}

func main () {
    cells := [512]int{}
    cells[1] = 1
    cells[34] = 1
    cells[64] = 1
    cells[65] = 1
    cells[66] = 1

    Display(cells)
    for {
        cells = Update(cells)
        Display(cells)
        fmt.Println()
        time.Sleep(20 * time.Millisecond)
    }
}
