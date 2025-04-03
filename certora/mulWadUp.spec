 
 
 
methods {

    function mulWadUp (uint256 x,uint256 y) external returns uint256 envfree ;
}
    // definition :  it is like marco in huff  , constant in solidity 
      definition WAD() returns uint256 = 1000000000000000000;
 
 
 
  rule check_HalmostestMulWadUpFuzz(uint256 x, uint256 y)  {
        // we tell that max_uint256/x must return uint256 .if we don't use x we can pass this max_uint256 directly without assert_uint256
        require(x == 0 || y == 0 || y <= assert_uint256(max_uint256/x)) ; // our precondition 
            uint256 result = mulWadUp(x, y);
            mathint expected = x * y == 0 ? 0 : (x * y - 1) / WAD() + 1;
            assert(result == assert_uint256(expected)); // our last check (can say invariant)
         
        
       
    }

    invariant mulWadUpInvariant(uint256 x, uint256 y) 
    mulWadUp(x, y) == assert_uint256(x * y == 0 ? 0 : (x * y - 1) / WAD() + 1)   // this is our single invariant sentence 
    // we can define pre condition which will be check before check the invariant single sentence like this : 
 // So we say "this invariant should be always true (hold) as long as the preserved block with its preconditions are true(hold)"
    {
        preserved {
             require(x == 0 || y == 0 || y <= assert_uint256(max_uint256/x)) ;
        }
    }