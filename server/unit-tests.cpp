#include <gtest/gtest.h>

#include "ttt-model.hpp"

typedef TicTacToeBoard TTTBoard;

TEST(TTTBoardTest, x_is_the_first_player)
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

TEST(TTTBoard, draw)
{
    TTTBoard board;

    //  X | O | X
    //  X | O | X
    //  O | X | O

    ASSERT_EQ(board.play(TTTBoard::Player::X, 0, 0), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::O, 1, 0), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::X, 2, 0), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::O, 0, 2), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::X, 1, 2), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::O, 2, 2), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::X, 0, 1), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::O, 1, 1), TTTBoard::PlayResult::NEXT_TURN);
    ASSERT_EQ(board.play(TTTBoard::Player::X, 2, 1), TTTBoard::PlayResult::DRAW);
}

TEST(TTTBoard, win_on_column)
{
    for(auto col_index = 0; col_index < 3; col_index++)
    {
        TTTBoard board;

        auto other_col = (col_index + 1) % 3;

        ASSERT_EQ(board.play(TTTBoard::Player::X, col_index, 0), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::O, other_col, 0), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::X, col_index, 1), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::O, other_col, 2), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::X, col_index, 2), TTTBoard::PlayResult::WINNER);
    }
}

TEST(TTTBoard, win_on_rows)
{
    for(auto row_index = 0; row_index < 3; row_index++)
    {
        TTTBoard board;

        auto other_row = (row_index + 1) % 3;

        ASSERT_EQ(board.play(TTTBoard::Player::X, 0, row_index), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::O, 0, other_row), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::X, 1, row_index), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::O, 2, other_row), TTTBoard::PlayResult::NEXT_TURN);
        ASSERT_EQ(board.play(TTTBoard::Player::X, 2, row_index), TTTBoard::PlayResult::WINNER);
    }
}



int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
