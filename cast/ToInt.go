package cast

import (
	"strconv"
)

func ToInt(s string) (int, error) {
	i, err := strconv.Atoi(s)
	if err != nil {
		return -1, err
	}
	return i, nil
}
