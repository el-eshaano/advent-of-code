package main

import (
	_ "embed"
	"fmt"
	"strings"

	"github.com/el-eshaano/advent-of-code/cast"
)

//go:embed input.txt
var rawInput string
var input [][]string

func spliceContains(splice []Range, val Range) bool {
	for _, v := range splice {
		if rangeEquals(v, val) {
			return true
		}
	}
	return false
}

func coordEquals(c1, c2 Coord) bool {
	return c1.Row == c2.Row && c1.Col == c2.Col
}

func rangeEquals(r1, r2 Range) bool {
	return coordEquals(r1.Min, r2.Min) && coordEquals(r1.Max, r2.Max)
}

type Coord struct {
	Row   int
	Col   int
	Value string
}

type Range struct {
	Min Coord
	Max Coord
}

func isDigit(s string) bool {
	return s[0] >= '0' && s[0] <= '9'
}

func init() {
	bylineInput := strings.Split(rawInput, "\n")
	for _, line := range bylineInput {
		input = append(input, strings.Split(line, ""))
	}
}

func getNeighbours(row, col int, input [][]string) []Coord {
	var neighbours []Coord
	for i := row - 1; i <= row+1; i++ {
		for j := col - 1; j <= col+1; j++ {
			if i < 0 || j < 0 || i >= len(input) || j >= len(input[i]) || (i == row && j == col) {
				continue
			}
			neighbours = append(neighbours, Coord{Row: i, Col: j, Value: input[i][j]})
		}
	}
	return neighbours
}

func getWholeNumber(c Coord) (int, Range) {
	var num string
	row, col := c.Row, c.Col

	for isDigit(input[row][col]) {
		col--
		if col < 0 {
			break
		}
	}
	col++
	min := Coord{Row: row, Col: col}

	for isDigit(input[row][col]) {
		num += input[row][col]
		col++
		if col >= len(input[row]) {
			break
		}
	}
	max := Coord{Row: row, Col: col}

	val, err := cast.StringToInt(num)
	if err != nil {
		panic(err)
	}
	return val, Range{Min: min, Max: max}
}

func part1() {

	uniqueNumbers := []Range{}
	sum := 0

	for i, line := range input {
		for j, char := range line {

			if isDigit(char) || char == "." {
				continue
			}
			neighbours := getNeighbours(i, j, input)
			for _, n := range neighbours {
				if isDigit(n.Value) {
					val, neighbourRange := getWholeNumber(n)
					isUnique := true
					for _, r := range uniqueNumbers {
						if rangeEquals(r, neighbourRange) {
							isUnique = false
							break
						}
					}
					if !isUnique {
						continue
					}
					uniqueNumbers = append(uniqueNumbers, neighbourRange)
					sum += val
				}
			}
		}
	}

	fmt.Println(sum)
}

func part2() {

	sum := 0

	for i, line := range input {
		for j, char := range line {

			if char == "*" {
				neighbours := getNeighbours(i, j, input)
				uniqueRanges := []Range{}
				uniqueVals := []int{}
				for _, neighbour := range neighbours {
					if isDigit(neighbour.Value) {
						val, range_ := getWholeNumber(neighbour)
						if spliceContains(uniqueRanges, range_) {
							continue
						}
						uniqueRanges = append(uniqueRanges, range_)
						uniqueVals = append(uniqueVals, val)
					}
				}
				if len(uniqueVals) == 2 {
					sum += uniqueVals[0] * uniqueVals[1]
				}
			}
		}
	}

	fmt.Println(sum)
}

func main() {
	part1()
	part2()
}
