package main

import (
	_ "embed"
	"fmt"
	"strings"

	"github.com/el-eshaano/advent-of-code/cast"
)

//go:embed test.txt
var rawInput string
var input []string

func init() {
	input = strings.Split(rawInput, "\n")
}

func main() {
	// part1()
	part2()
}

func part1() {

	sum := 0

	for _, line := range input {

		firstDigit := -1
		lastDigit := -1

		for _, char := range line {
			digit, err := cast.StringToInt(string(char))
			if err != nil {
				continue
			}
			if firstDigit == -1 {
				firstDigit = digit
			}
			lastDigit = digit
		}

		res, err := cast.StringToInt(fmt.Sprintf("%d%d", firstDigit, lastDigit))
		if err != nil {
			continue
		}
		sum += res
	}

	fmt.Println(sum)
}

func part2() {

	sum := 0

	for _, line := range input {

		line = strings.ReplaceAll(line, "one", "one1one")
		line = strings.ReplaceAll(line, "two", "two2two")
		line = strings.ReplaceAll(line, "three", "three3three")
		line = strings.ReplaceAll(line, "four", "four4four")
		line = strings.ReplaceAll(line, "five", "five5five")
		line = strings.ReplaceAll(line, "six", "six6six")
		line = strings.ReplaceAll(line, "seven", "seven7seven")
		line = strings.ReplaceAll(line, "eight", "eight8eight")
		line = strings.ReplaceAll(line, "nine", "nine9nine")
		line = strings.ReplaceAll(line, "zero", "zero0zero")

		firstDigit := -1
		lastDigit := -1

		for _, char := range line {
			digit, err := cast.StringToInt(string(char))
			if err != nil {
				continue
			}
			if firstDigit == -1 {
				firstDigit = digit
			}
			lastDigit = digit
		}

		res, err := cast.StringToInt(fmt.Sprintf("%d%d", firstDigit, lastDigit))
		if err != nil {
			continue
		}
		sum += res
	}

	fmt.Println(sum)

}
