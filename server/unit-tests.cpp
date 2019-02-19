#include <gtest/gtest.h>

#include "ttt-model.hpp"

TEST(TTTBoard, x_is_the_first_player)
{
    TicTacToeBoard board;

    ASSERT_EQ(board.next_player(), TicTacToeBoard::Player::X);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
