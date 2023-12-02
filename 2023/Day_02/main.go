package main

import (
	_ "embed"
	"fmt"
	"strings"

	"github.com/el-eshaano/advent-of-code/cast"
)

//go:embed input.txt
var rawInput string

type Game struct {
	red   int
	green int
	blue  int
}

type GameSet struct {
	id    int
	games []Game
}

func parseGame(input string) GameSet {

	gameIdString, gameString := strings.Split(input, ":")[0], strings.Split(input, ":")[1]
	id, err := cast.ToInt(gameIdString[5:])
	if err != nil {
		panic(err)
	}

	var games []Game
	for _, game := range strings.Split(gameString, ";") {
		red, green, blue := 0, 0, 0
		for _, color := range strings.Split(game, ",") {
			if strings.Contains(color, "red") {
				red, _ = cast.ToInt(strings.Split(color, " ")[1])
			} else if strings.Contains(color, "green") {
				green, _ = cast.ToInt(strings.Split(color, " ")[1])
			} else if strings.Contains(color, "blue") {
				blue, _ = cast.ToInt(strings.Split(color, " ")[1])
			}
		}
		games = append(games, Game{red: red, green: green, blue: blue})
	}

	return GameSet{id: id, games: games}
}

func isValidGameSet(gameSet GameSet, trueGame Game) bool {

	for _, game := range gameSet.games {
		if game.red > trueGame.red || game.green > trueGame.green || game.blue > trueGame.blue {
			return false
		}
	}

	return true

}

func part1() {
	trueGame := Game{red: 12, green: 13, blue: 14}
	inputs := strings.Split(rawInput, "\n")

	// each input is of the form "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

	sum := 0

	for _, input := range inputs {
		gameSet := parseGame(input)
		if isValidGameSet(gameSet, trueGame) {
			sum += gameSet.id
		}
	}

	fmt.Println(sum)
}

func gamePower(g GameSet) int {
	maxR := 1
	maxG := 1
	maxB := 1

	for _, game := range g.games {
		if game.red > maxR {
			maxR = game.red
		}
		if game.green > maxG {
			maxG = game.green
		}
		if game.blue > maxB {
			maxB = game.blue
		}
	}

	fmt.Printf("Game %d: %d %d %d\n", g.id, maxR, maxG, maxB)

	return int(maxB * maxG * maxR)
}

func part2() {
	inputs := strings.Split(rawInput, "\n")

	sum := 0

	for _, input := range inputs {
		gameSet := parseGame(input)
		sum += gamePower(gameSet)
	}

	fmt.Println(sum)
}

func main() {
	// part1()
	part2()
}
