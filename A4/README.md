const {
  convertAll
} = require('bpmn-to-image');

await convertAll([
  {
    input: 'flowchart .bpmn',
    outputs: [
      'diagram.pdf',
      'diagram.png'
      'diagram.svg'
    ]
  }
]);
