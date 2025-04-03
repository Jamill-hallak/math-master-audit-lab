

methods {

    // function uniSqrt(uint256) external  returns uint256 envfree ;
    // function mathMastersSqrt(uint256) external  returns uint256 envfree ;

    function mathMasterTopHalf(uint256) external returns uint256 envfree ;
    function solmatTopHalf(uint256) external returns uint256 envfree ;

}
//  rule uniSqrtMatchesMathMastersSqrt(uint256 x)  {
//         assert(mathMastersSqrt(x) == uniSqrt(x));
//     }

rule solmatTopHalfMatchesmathMasterTopHalf(uint256 x) {
    assert(mathMasterTopHalf(x) == solmatTopHalf(x)) ;
}