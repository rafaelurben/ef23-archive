//*******************************************************/
// Functions
//*******************************************************/


// Pythagoras
function getHypotenuse(a, b) {
	return (a*a + b*b) ** 0.5
}
const hypo = getHypotenuse(3, 4)  // c is now: 5
console.log(hypo);


// convert to seconds
function getSeconds(hours, minutes, seconds) {
	return ((hours*60)+minutes)*60+seconds;
}
const oneLesson = getSeconds(0, 45, 0) // should return 2700
console.log(oneLesson);


//Create HTML heading tag
function createHeading(text) {
	return `<h1>${text}</h1>`
}
const heading = createHeading("Welcome") // should return "<h1>Welcome</h1>"
console.log(heading);


//Create SVG rect
function createSvgRect(x, y, w, h) {
	return `<rect x="${x}" y="${y} width="${w}" height="${h}"></rect>`
}
const svgRect = createSvgRect(100, 200, 300, 400) // should return "<rect x='100' y='200' width='300' height='400'></rect>"
console.log(svgRect);


// Find median of 3 values
function medianOf3(a, b, c) {
	return a<b && b<c ? b : (a<c && c<b ? c : (b<c && c<a ? c : (b<a && a<c ? a : (c<a && a<b ? a : b))));
}
const m = medianOf3(8, 11, 9) // should return 9
console.log(m);


// Find average of 3 values
function averageOf3(a, b, c) {
	return (a+b+c)/3;
}
const a = averageOf3(4, 11, 9) // should return 8
console.log(a);


// Find average of array
function getAverage(array) {
	result = 0;
	array.forEach(elem => {result = result+elem});
	return result/array.length;
}
const b = getAverage([4, 11, 9, 2, 9]) // should return 7
console.log(b);


// Solve ax^2 + bx + c = 0
function solveQuadratic(a, b, c) {
	//@TODO
	return 
}
const solutions = solveQuadratic(1, 0, -16) // should return [-4, 4]
const solution = solveQuadratic(1, -2, 1) // should return [1]
const empty = solveQuadratic(1, 0, 16) // should return []

console.log(solutions, solution, empty);
