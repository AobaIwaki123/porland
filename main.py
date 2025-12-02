from operator import add, sub, truediv, mul


def evaluate_rpn(expression: str) -> float:
    """
    逆ポーランド記法（RPN）の式を評価します。
    
    Args:
        expression: 演算子と数値からなる文字列
        
    Returns:
        計算結果
        
    Raises:
        ValueError: 式が無効な場合
    """
    # 演算子とその関数のマッピング
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }
    
    stack = []
    
    for char in expression:
        if char in operators:
            # スタックに十分な要素があるか確認
            if len(stack) < 2:
                raise ValueError(f"無効な式: 演算子 '{char}' に対してオペランドが不足しています")
            
            # 2つのオペランドをポップ（順序に注意）
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # 演算を実行
            result = operators[char](operand1, operand2)
            stack.append(result)
        else:
            # 数値として解析
            try:
                stack.append(int(char))
            except ValueError:
                raise ValueError(f"無効な文字: '{char}'")
    
    # 最終的にスタックには1つの要素だけが残るべき
    if len(stack) != 1:
        raise ValueError(f"無効な式: 計算後にスタックに {len(stack)} 個の要素が残っています")
    
    return stack[0]
