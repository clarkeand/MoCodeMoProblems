/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    // Define a mapping for each Roman numeral
    const romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let total = 0;
    for(let i = 0; i < s.length; i++) {
        // If the current numeral is smaller than the next one, subtract its value from the total
        if(romanMap[s[i]] < romanMap[s[i+1]]) {
            total -= romanMap[s[i]];
        } else {
            // Otherwise, add its value to the total
            total += romanMap[s[i]];
        }
    }
    
    return total;
};