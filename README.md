1. Compile `main.py` we will get  `main.avm` through `NEO compiler (NEO-boa)` 
2. build `smartContracts/SCL-token/main.py`
3. Deploy through private net with the command:
    `$import contract smartContracts/SCL-token/main.avm 071010 05 true true true`
4. Working with smart contract with the command :
`$testinvoke scriptHash nameFunction paramater`
