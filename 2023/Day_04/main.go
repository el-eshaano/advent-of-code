package main

import (
	_ "embed"
	"fmt"
	"math"
	"strings"

	"github.com/el-eshaano/advent-of-code/cast"
)

//go:embed input.txt
var rawInput string
var cardsStrings []string
var cards []Card

type Card struct {
	WinningNumbers []int
	CardNumbers    []int
	Id             int
	Score          float64
	MatchingCount  int
}

func (c *Card) GetScore() float64 {
	var count int
	for _, winningNumber := range c.WinningNumbers {
		for _, cardNumber := range c.CardNumbers {
			if winningNumber == cardNumber {
				count++
			}
		}
	}
	c.MatchingCount = count
	if count == 0 {
		c.Score = 0
		return 0
	}

	c.Score = math.Pow(2, float64(count-1))
	return c.Score
}

func init() {
	cardsStrings = strings.Split(rawInput, "\n")

	for _, game := range cardsStrings {
		idString, numbersString := strings.Split(game, ": ")[0], strings.Split(game, ": ")[1]
		s := strings.Split(idString, " ")
		id, err := cast.StringToInt(s[len(s)-1])
		if err != nil {
			panic(err)
		}

		winningNumbersString, cardNumbersString := strings.Split(numbersString, "|")[0], strings.Split(numbersString, "|")[1]
		winningNumbers := strings.Split(winningNumbersString, " ")
		cardNumbers := strings.Split(cardNumbersString, " ")

		cards = append(cards, Card{
			WinningNumbers: cast.StringSliceToIntSlice(winningNumbers),
			CardNumbers:    cast.StringSliceToIntSlice(cardNumbers),
			Id:             id,
		})
	}
	for i := range cards {
		cards[i].GetScore()
	}
}

func part1() {
	var totalScore float64
	for _, card := range cards {
		totalScore += card.Score
	}
	fmt.Println(totalScore)
}

func part2() {

	cardCount := make([]int, len(cards))
	for i := range cardCount {
		cardCount[i] = 1
	}

	cardCount[0] = 1
	for cardIndex, c := range cards {

		for i := cardIndex + 1; i <= cardIndex+c.MatchingCount; i++ {
			cardCount[i] += cardCount[cardIndex]
		}
	}

	sum := 0
	for _, v := range cardCount {
		sum += v
	}
	// fmt.Println(cardCount)
	fmt.Println(sum)
}

func main() {
	// part1()
	part2()
}
