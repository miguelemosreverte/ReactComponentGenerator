componentName=$1
path=$2

echo "import React from 'react';
import ReactDOM from 'react-dom';
import $componentName from './$componentName';

it('$componentName initial render', () => {
  const div = document.createElement('div');
  ReactDOM.render(<$componentName />, div);
  ReactDOM.unmountComponentAtNode(div);
});" > $path/$componentName/$componentName.test.js