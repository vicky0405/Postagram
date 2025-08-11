import React, { useState } from "react";
import { Button, Modal, Form, Dropdown } from "react-bootstrap";
import axiosService from "../../helpers/axios";
import Toaster from "../Toaster";

function UpdatePost(props) {
  const { post, refresh } = props;
  const [show, setShow] = useState(false);
  const [showToast, setShowToast] = useState(false);
  const [validated, setValidated] = useState(false);
  const [form, setForm] = useState({
    author: post.author.id,
    body: post.body,
  });

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleSubmit = (event) => {
    event.preventDefault();
    const updatePostForm = event.currentTarget;

    if (updatePostForm.checkValidity() === false) {
      event.stopPropagation();
    }

    setValidated(true);

    const data = {
      author: form.author,
      body: form.body,
    };

    axiosService
      .put(`api/post/${post.id}/`, data)
      .then(() => {
        handleClose();
        setShowToast(true);
        refresh();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <>
      <Dropdown.Item data-testid="show-modal-form" onClick={handleShow}>Modify</Dropdown.Item>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton className="border-0">
          <Modal.Title>Update Post</Modal.Title>
        </Modal.Header>
        <Modal.Body className="border-0">
          <Form noValidate validated={validated} onSubmit={handleSubmit} data-testid="update-post-form">
            <Form.Group className="mb-3">
              <Form.Control
                name="body"
                value={form.body}
                data-testid="post-body-field"
                onChange={(e) => setForm({ ...form, body: e.target.value })}
                as="textarea"
                rows={3}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button data-testid="update-post-submit" variant="primary" onClick={handleSubmit}>
            Modify
          </Button>
        </Modal.Footer>
      </Modal>
      <Toaster
        title="Success!"
        message="Post updated 🚀"
        type="success"
        showToast={showToast}
        onClose={() => setShowToast(false)}
      />
    </>
  );
}

export default UpdatePost;