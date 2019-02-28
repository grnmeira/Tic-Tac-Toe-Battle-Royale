#include <gtest/gtest.h>

#include "ttt-model.hpp"

typedef TicTacToeBoard TTTBoard;

TEST(TTTBoard, x_is_the_first_player)
{
    TTTBoard board;

    ASSERT_EQ(board.next_player(), TTTBoard::Player::X);
}

TEST(TTTBoard, o_is_the_next_player)
{
    TTTBoard board;

    ASSERT_EQ(board.next_player(), TTTBoard::Player::X);

    auto result = board.play(TTTBoard::Player::X, 1, 1);

    ASSERT_EQ(result, TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.next_player(), TTTBoard::Player::O);
}

TEST(TTTBoard, cant_play_same_tile_twice)
{
    TTTBoard board;

    ASSERT_EQ(board.next_player(), TTTBoard::Player::X);

    ASSERT_EQ(board.play(TTTBoard::Player::X, 1, 1), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::O, 1, 1), TTTBoard::PlayResult::INVALID_PLAY);
}

TEST(TTTBoard, invalid_player_on_next_turn)
{
    TTTBoard board;

    ASSERT_EQ(board.next_player(), TTTBoard::Player::X);

    ASSERT_EQ(board.play(TTTBoard::Player::X, 1, 1), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::X, 2, 2), TTTBoard::PlayResult::INVALID_PLAY);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
