import React from 'react';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';
import { Container, Row, Col } from 'react-bootstrap';

function App() {
    return (
        <div className="App">
            <Container>
                <Row>
                    <Col>
                        <h1><u>PRODUCT LIST </u></h1>
                        <ProductList />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <h1><u>ADD PRODUCT</u></h1>
                        <ProductForm />
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default App;
