import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Modal, Button, Form, Alert, Spinner } from 'react-bootstrap';

const ProductUpdateForm = ({ show, handleClose, productId, onUpdate }) => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [price, setPrice] = useState('');
    const [success, setSuccess] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchProduct = async () => {
            if (productId) {
                setLoading(true);
                try {
                    const response = await axios.get(`http://localhost:8000/products/products/${productId}/`);
                    const product = response.data;
                    setName(product.name);
                    setDescription(product.description);
                    setPrice(product.price);
                } catch (error) {
                    setError(error.message);
                } finally {
                    setLoading(false);
                }
            }
        };

        fetchProduct();
    }, [productId]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.put(`http://localhost:8000/products/products/${productId}/`, {
                name,
                description,
                price
            });
            onUpdate(response.data);
            setSuccess('Product Details Updated successfully');
            handleClose();
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Update Product</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                {error && <Alert variant="danger">{error}</Alert>}
                {loading ? (
                    <Spinner animation="border" role="status">
                        <span className="sr-only">Loading...</span>
                    </Spinner>
                ) : (
                    <Form onSubmit={handleSubmit}>
                        <Form.Group>
                            <Form.Label>Name</Form.Label>
                            <Form.Control type="text" value={name} onChange={(e) => setName(e.target.value)} required />
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Description</Form.Label>
                            <Form.Control as="textarea" value={description} onChange={(e) => setDescription(e.target.value)} required />
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Price</Form.Label>
                            <Form.Control type="number" value={price} onChange={(e) => setPrice(e.target.value)} required />
                        </Form.Group><br></br>
                        <Button type="submit" variant="primary">Update Product</Button>
                        {success && <Alert variant="success">{success}</Alert>}
                    </Form>
                )}
            </Modal.Body>
        </Modal>
    );
};

export default ProductUpdateForm;
