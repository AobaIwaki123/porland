import pytest
from main import porland


def test_simple_addition():
    """テスト対象: 1 + 1 = 2"""
    # 逆ポーランド記法: 11+
    result = porland("11+")
    assert result == 2


def test_simple_subtraction():
    """テスト対象: 5 - 3 = 2"""
    # 逆ポーランド記法: 53-
    result = porland("53-")
    assert result == 2


def test_simple_multiplication():
    """テスト対象: 3 * 4 = 12"""
    # 逆ポーランド記法: 34*
    result = porland("34*")
    assert result == 12


def test_simple_division():
    """テスト対象: 8 / 2 = 4"""
    # 逆ポーランド記法: 82/
    result = porland("82/")
    assert result == 4


def test_complex_expression_1():
    """テスト対象: (1 + 2) * 3 = 9"""
    # 逆ポーランド記法: 12+3*
    result = porland("12+3*")
    assert result == 9


def test_complex_expression_2():
    """テスト対象: (5 + 3) / 2 = 4"""
    # 逆ポーランド記法: 53+2/
    result = porland("53+2/")
    assert result == 4


def test_complex_expression_3():
    """テスト対象: (9 - 3) / 2 = 3"""
    # 逆ポーランド記法: 93-2/
    result = porland("93-2/")
    assert result == 3


def test_complex_expression_4():
    """テスト対象: 2 * (3 + 4) = 14"""
    # 逆ポーランド記法: 234+*
    result = porland("234+*")
    assert result == 14


def test_multiple_operations():
    """テスト対象: ((1 + 2) * (3 + 4)) = 21"""
    # 逆ポーランド記法: 12+34+*
    result = porland("12+34+*")
    assert result == 21

