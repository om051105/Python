from solution import maskify
import codewars_test as test

@test.describe('Sample tests')
def sample_tests():
    @test.it("masking: ''")
    def test1():
        test.assert_equals(maskify(''), '')
    
    @test.it("masking: '123'")
    def test2():
        test.assert_equals(maskify('123'), '123')
    
    @test.it("masking: 'SF$SDfgsd2eA'")
    def test3():
        test.assert_equals(maskify('SF$SDfgsd2eA'), '########d2eA')