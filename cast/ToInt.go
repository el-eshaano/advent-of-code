package cast

import (
	"strconv"
)

func StringToInt(s string) (int, error) {
	i, err := strconv.Atoi(s)
	if err != nil {
		return -1, err
	}
	return i, nil
}

func StringSliceToIntSlice(s []string) []int {
	var i []int
	for _, v := range s {
		if v == "" {
			continue
		}
		integer, err := StringToInt(v)
		if err != nil {
			panic(err)
		}
		i = append(i, integer)
	}
	return i
}
