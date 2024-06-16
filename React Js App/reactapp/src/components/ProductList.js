import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Spinner, Alert, Button, Form } from 'react-bootstrap';
import ProductUpdateForm from './ProductUpdateForm';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const [showUpdateModal, setShowUpdateModal] = useState(false);
    const [selectedProductId, setselectedProductId] = useState(null);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/products/products/`);
                setProducts(response.data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchProducts();
    }, []);

    const handleDelete = async (id) => {
        try {
            await axios.delete(`http://localhost:8000/products/products/${id}/`);
            setProducts(products.filter(Product => Product.id !== id));
            setSuccess('Product removed successfully');
        } catch (error) {
            setError(error.message);
        }
    };
    const handleShowUpdateModal = (productId) => {
        setselectedProductId(productId);
        setShowUpdateModal(true);
    };

    const handleUpdate = (updatedProduct) => {
        setProducts(products.map(Product => (Product.id === updatedProduct.id ? updatedProduct : Product)));
    };
    if (loading) return <Spinner animation="border" role="status"><span className="sr-only">Loading...</span></Spinner>;
    if (error) return <Alert variant="danger">Error: {error}</Alert>;
    

    return (
        <Container>
           <Form onSubmit={handleDelete}>
                {success && <Alert variant="success">{success}</Alert>}
            <Row>
                {products.map(Product => (
                    <Col key={Product.id} md={4} className="mb-3">
                        <Card>
                            <Card.Body>
                                <Card.Title>{Product.name}</Card.Title>
                                <Card.Text>{Product.description}</Card.Text>
                                <Card.Text>Price: ${Product.price}</Card.Text>
                                <Button variant="danger" onClick={() => handleDelete(Product.id)}>Delete</Button> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <Button variant="warning" onClick={() => handleShowUpdateModal(Product.id)}>Update</Button>                               
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
            </Form>
            {selectedProductId && (
                <ProductUpdateForm
                    show={showUpdateModal}
                    handleClose={() => setShowUpdateModal(false)}
                    productId={selectedProductId}
                    onUpdate={handleUpdate}
                />
            )}
        </Container>
        
    );
    if (success) return <Alert variant="success">{success}</Alert>;
};

export default ProductList;
