

# train_cws.txt 分词训练文本
# test_cws1.txt 正确分词的分词预测文本移除空格后得到测试raw文本 @row_cws.txt
# 用train_cws.txt训练后，得到的参数用于 移除空格后的测试raw文本 @row_cws.txt 得到 @test_cws2.txt 分词测试文本
# test_cws2.txt 分词测试文本


# 将test_cws1.txt 正确分词的分词预测文本转化为word-label格式的文本 @test_cws.txt
# 将test_cws2.txt 分词测试文本转化为word-label格式的文本 @test_cws3.txt

# 通过 @test_cws.txt 和 @test_cws3.txt 评价分词模型